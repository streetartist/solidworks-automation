# RollBy Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RollBy`

Rolls the model view about the line of sight by the specified angle.
Rolls the model view about the line of sight by the specified angle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RollBy( _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IModelView
Dim Angle As System.Double
 
instance.RollBy(Angle)
```

```

void RollBy( 
   System.double Angle
)
```

```

void RollBy( 
   System.double Angle
) 
```

#### Parameters

*Angle*
:   Angle by which to roll the model view about the line of sight

Example

[Roll Model View (VBA)](Roll_Model_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
