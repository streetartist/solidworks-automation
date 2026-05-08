# DeleteStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle`

Deletes the specified style.
Deletes the specified style.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteStyle( _
   ByVal StyleName As System.String _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim StyleName As System.String
Dim value As System.Boolean
 
value = instance.DeleteStyle(StyleName)
```

```

System.bool DeleteStyle( 
   System.string StyleName
)
```

```

System.bool DeleteStyle( 
   System.String^ StyleName
) 
```

#### Parameters

*StyleName*
:   Name of the style to delete

#### Return Value

True if the operation succeeds, false if it fails

Remarks

The current styleis set to <NONE>. Dimensions and annotations retain the properties previously applied by the style unless the items are [reset to the document default](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.md)  
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.md)  
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.md)  
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.md)  
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.md)  
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.md)
