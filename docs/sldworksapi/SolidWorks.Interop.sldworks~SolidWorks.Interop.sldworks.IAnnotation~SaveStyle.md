# SaveStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle`

Saves the specified style.
Saves the specified style.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveStyle( _
   ByVal StyleName As System.String, _
   ByVal PathName As System.String _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim StyleName As System.String
Dim PathName As System.String
Dim value As System.Boolean
 
value = instance.SaveStyle(StyleName, PathName)
```

```

System.bool SaveStyle( 
   System.string StyleName,
   System.string PathName
)
```

```

System.bool SaveStyle( 
   System.String^ StyleName,
   System.String^ PathName
) 
```

#### Parameters

*StyleName*
:   Name of the style

*PathName*
:   Path and filename to which to save the style

Remarks

See SOLIDWORKS Help for the filename extensions to use for styles.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.md)  
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.md)  
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.md)  
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.md)  
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.md)  
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.md)
