# UserFavors Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UserFavors`

Specifies whether geometric relations are automatically created as you add sketch entities.
Specifies whether geometric relations are automatically created as you add sketch entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UserFavors() 
```

```

Dim instance As IModelDoc2
 
instance.UserFavors()
```

```

void UserFavors()
```

```

void UserFavors(); 
```

Remarks

If this option is on, then the cursor changes shape as you sketch to show you which relations can be created: horizontal, vertical, parallel, perpendicular, tangent, midpoint, or coincident.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
