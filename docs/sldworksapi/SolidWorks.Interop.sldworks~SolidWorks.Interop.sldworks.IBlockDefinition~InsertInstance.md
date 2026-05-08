# InsertInstance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~InsertInstance`

Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.
Obsolete. Superseded by [ISketchManager::InsertSketchBlockInstance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchBlockInstance.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertInstance( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double _
) As BlockInstance
```

```

Dim instance As IBlockDefinition
Dim X As System.Double
Dim Y As System.Double
Dim Angle As System.Double
Dim Scale As System.Double
Dim value As BlockInstance
 
value = instance.InsertInstance(X, Y, Angle, Scale)
```

```

BlockInstance InsertInstance( 
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
)
```

```

BlockInstance^ InsertInstance( 
   System.double X,
   System.double Y,
   System.double Angle,
   System.double Scale
) 
```

#### Parameters

*X*

*Y*

*Angle*

*Scale*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.md)  
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.md)
