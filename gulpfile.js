var gulp = require('gulp');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var autoprefixer = require('autoprefixer');
var concat = require('gulp-concat');
var postcss = require('gulp-postcss');
var cleanCSS = require('gulp-clean-css');
var sourcemaps = require('gulp-sourcemaps');
var browserSync = require('browser-sync');
var pump = require('pump');

gulp.task('scripts', function() {
  gulp
    .src([
      'node_modules/jquery/dist/jquery.js',
      // 'node_modules/moment/moment.js',
      'node_modules/moment/min/moment-with-locales.min.js',
      'node_modules/bootstrap/dist/js/bootstrap.js',
      'node_modules/tempusdominus-bootstrap-4/build/js/tempusdominus-bootstrap-4.min.js',
      './src/assets/js/**/*.js' // our js files
    ])
    .pipe(concat('main.js')) // cancatenation to file myproject.js
    .pipe(uglify()) // uglifying this file
    .pipe(rename({ suffix: '.min' })) // renaming file to myproject.min.js
    .pipe(gulp.dest('./src/static_in_env/js')); // save file to destination directory
});

gulp.task('sass', function() {
  gulp
    .src('./src/assets/scss/main.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(sass({ includePaths: ['./src/assets/scss'] }))
    .pipe(concat('style.min.css'))
    .pipe(sourcemaps.init())
    .pipe(postcss([autoprefixer()]))
    .pipe(cleanCSS())
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest('./src/static_in_env/css'));
});

gulp.task('font_awesome', function() {
  return gulp
    .src('./node_modules/font-awesome/fonts/*.*')
    .pipe(gulp.dest('./src/static_in_env/fonts'));
});

gulp.task('browser-sync', function() {
  browserSync.init(
    [
      './src/static_in_env/css/*.css',
      './src/assets/js/*.js',
      './src/templates/**/*.html',
      './src/**/*.py'
    ],
    {
      host: '192.168.1.136',
      notify: true,
      proxy: 'localhost:8000'
    }
  );
});

gulp.task('uglify-error-debugging', function(cb) {
  pump(
    [
      gulp.src('./src/assets/js/**/*.js'),
      uglify(),
      gulp.dest('./src/static_in_env/js')
    ],
    cb
  );
});

gulp.task('default', ['scripts', 'sass', 'browser-sync'], function() {
  gulp.watch('./src/assets/scss/**/*.scss', ['sass']);
  gulp.watch('./src/assets/js/**/*.js', ['scripts']);
});
