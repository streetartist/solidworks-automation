# IAnnotationView Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members`

Allows access to annotation views in parts and assemblies.
The following tables list the members exposed by [IAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [Always2D](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Always2D.md) | Gets whether to display annotations in 2D or 3D. |
| Property | [AngleMadeWithViewHorizontal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AngleMadeWithViewHorizontal.md) | Gets the angle used to make the annotation view horizontal. |
| Property | [AnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~AnnotationCount.md) | Gets the number of [annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) in this annotation view. |
| Property | [Annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.md) | Obsolete. Superseded by [IAnnotationView::GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.md). |
| Property | [FlatPatternView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~FlatPatternView.md) | Gets whether this annotation view is a flat-pattern view. |
| Property | [UnassignedView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~UnassignedView.md) | Gets whether this annotation view is assigned to a 3D View. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Activate.md) | Activates this annotation view. |
| Method | [ActivateAndReorient](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~ActivateAndReorient.md) | Activates and reorients this annotation view. |
| Method | [GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.md) | Gets the annotations in this annotation view. |
| Method | [GetViewRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetViewRotation.md) | Gets the rotation matrix of the annotation view relative to the X-Y plane of the model. |
| Method | [Hide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Hide.md) | Hides the annotations in an annotation view that is not activated. |
| Method | [IGetAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations.md) | Obsolete. Superseded by [IAnnotationView::GetAnnotations2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~GetAnnotations2.md). |
| Method | [IGetViewRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetViewRotation.md) | Gets the rotation matrix of the annotation view relative to the X-Y plane of the model. |
| Method | [IsShown](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IsShown.md) | Gets whether the annotations in this annotation view are shown. |
| Method | [MoveAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~MoveAnnotations.md) | Moves the specified annotations to this annotation view. |
| Method | [Orient](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Orient.md) | Orients this annotation view. |
| Method | [Show](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Show.md) | Shows the annotations in an annotation view that is not activated. |

[Top](#top)

 

See Also

#### Reference

[IAnnotationView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)
