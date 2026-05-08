# EditOrdinate Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditOrdinate`

Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group.
Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditOrdinate() 
```

```

Dim instance As IModelDoc2
 
instance.EditOrdinate()
```

```

void EditOrdinate()
```

```

void EditOrdinate(); 
```

Remarks

You must pre-select the existing ordinate dimension and the entities to which to dimension. The position of the text and type of ordinate is determined by the existing ordinate dimension.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.md)  
[IModelDoc2::ReattachOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReattachOrdinate.md)  
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.md)
