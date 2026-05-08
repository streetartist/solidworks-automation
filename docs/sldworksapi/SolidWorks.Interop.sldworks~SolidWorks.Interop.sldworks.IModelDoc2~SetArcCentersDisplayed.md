# SetArcCentersDisplayed Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetArcCentersDisplayed`

Sets the current arc centers displayed setting.
Sets the current arc centers displayed setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetArcCentersDisplayed( _
   ByVal Setting As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Setting As System.Boolean
 
instance.SetArcCentersDisplayed(Setting)
```

```

void SetArcCentersDisplayed( 
   System.bool Setting
)
```

```

void SetArcCentersDisplayed( 
   System.bool Setting
) 
```

#### Parameters

*Setting*
:   True to display arc centers, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetArcCentersDisplayed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetArcCentersDisplayed.md)
