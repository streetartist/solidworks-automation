# GetSpecificManipulator Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~GetSpecificManipulator`

Gets the manipulator for this SOLIDWORKS part or assembly document.
Gets the manipulator for this SOLIDWORKS part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSpecificManipulator() As System.Object
```

```

Dim instance As IManipulator
Dim value As System.Object
 
value = instance.GetSpecificManipulator()
```

```

System.object GetSpecificManipulator()
```

```

System.Object^ GetSpecificManipulator(); 
```

#### Return Value

- [ITriadManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.md)
- [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)
- [IPlaneManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.md)

Example

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)  
[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)  
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)  
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.md)
