# GetPosition Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition`

Gets the position of this annotation.
Gets the position of this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPosition() As System.Object
```

```

Dim instance As IAnnotation
Dim value As System.Object
 
value = instance.GetPosition()
```

```

System.object GetPosition()
```

```

System.Object^ GetPosition(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The retval is an array of 3 doubles, the x, y, z origin of the annotation.

If this method is not successful in retrieving the position of the annotation in Visual Basic for Applications (VBA), then the VARIANT SafeArray is empty (OLE Automation only), or the status value is S\_false (COM only). Make sure that you check this value before using the returned position.

The following table lists the types of annotations that this method supports and the position of the x, y, z origin. In a drawing, the x, y, z origin is relative to the origin of the drawing sheet (the lower-left corner of the sheet).

|  |  |
| --- | --- |
| Type of Annotation | Position of XYZ Origin |
| [Datum Feature Symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md) | Point where leader hits symbol |
| [Datum Target Symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md) | Centerpoint of the circle that is attached to the leader |
| [Display Dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) | Point of leader attachment centered on a text box border / center point of bottom border of text box |
| [Geometric Tolerances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md) | Upper-left corner of the symbol |
| [Notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md) | Upper-left corner of the text box |
| [Surface Finish Symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md) | Lower-left point of symbol |
| [Table Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md) | Position of x,y,z determined by [ITableAnnotation::AnchorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~AnchorType.md) |
| [Weld Symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) | Left endpoint of the main horizontal line in the symbol |

If you use this method on any other types of annotations, SOLIDWORKS takes no action and returns false.

Example

[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)  
[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)  
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)  
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::IGetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetPosition.md)  
[IAnnotation::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md)  
[INote::LockPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.md)
