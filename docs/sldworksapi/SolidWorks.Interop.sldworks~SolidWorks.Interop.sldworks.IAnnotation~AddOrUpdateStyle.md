# AddOrUpdateStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle`

Adds or updates the annotation linked to the specified style.
Adds or updates the annotation linked to the specified style.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddOrUpdateStyle( _
   ByVal StyleName As System.String, _
   ByVal BreakLinks As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim StyleName As System.String
Dim BreakLinks As System.Boolean
Dim value As System.Boolean
 
value = instance.AddOrUpdateStyle(StyleName, BreakLinks)
```

```

System.bool AddOrUpdateStyle( 
   System.string StyleName,
   System.bool BreakLinks
)
```

```

System.bool AddOrUpdateStyle( 
   System.String^ StyleName,
   System.bool BreakLinks
) 
```

#### Parameters

*StyleName*
:   Name of the style to add or update

*BreakLinks*
:   True to break all links to this style, false to not

#### Return Value

Ture if the operation succeeds, false if it fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.md)  
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.md)  
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.md)  
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.md)  
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.md)  
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.md)
