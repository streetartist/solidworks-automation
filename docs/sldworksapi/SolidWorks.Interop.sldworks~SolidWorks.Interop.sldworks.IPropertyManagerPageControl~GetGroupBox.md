# GetGroupBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~GetGroupBox`

Gets the PropertyManager group box to which this control belongs.
Gets the PropertyManager group box to which this control belongs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGroupBox() As PropertyManagerPageGroup
```

```

Dim instance As IPropertyManagerPageControl
Dim value As PropertyManagerPageGroup
 
value = instance.GetGroupBox()
```

```

PropertyManagerPageGroup GetGroupBox()
```

```

PropertyManagerPageGroup^ GetGroupBox(); 
```

#### Return Value

[PropertyManager page group box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup.md) or NULL if the control is not in a PropertyManager group box

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
