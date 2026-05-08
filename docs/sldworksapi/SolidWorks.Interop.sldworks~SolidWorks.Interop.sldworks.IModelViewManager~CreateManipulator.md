# CreateManipulator Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateManipulator`

Creates a manipulator, which is similar to the triad in the SOLIDWORKS user interface.
Creates a manipulator, which is similar to the triad in the SOLIDWORKS user interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateManipulator( _
   ByVal Type As System.Integer, _
   ByVal PHandler As System.Object _
) As Manipulator
```

```

Dim instance As IModelViewManager
Dim Type As System.Integer
Dim PHandler As System.Object
Dim value As Manipulator
 
value = instance.CreateManipulator(Type, PHandler)
```

```

Manipulator CreateManipulator( 
   System.int Type,
   System.object PHandler
)
```

```

Manipulator^ CreateManipulator( 
   System.int Type,
   System.Object^ PHandler
) 
```

#### Parameters

*Type*
:   Type of manipulator to create as defined by [swManipulatorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swManipulatorType_e.html)

*PHandler*
:   Manipulator handler object

#### Return Value

[Manipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)

Remarks

If you move a manipulator far away from the model and then zoom-to-fit the model, the manipulator is not seen because it is not included in the clipping region.

See [Manipulators](sldworksapiprogguide.chm::/overview/Manipulators.htm) for details.

Example

[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)  
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)  
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)  
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)  
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)  
[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)
