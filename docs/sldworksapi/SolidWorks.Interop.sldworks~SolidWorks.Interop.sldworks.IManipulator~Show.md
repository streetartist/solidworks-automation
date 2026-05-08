# Show Method (IManipulator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator~Show`

Shows the manipulator in this SOLIDWORKS part or assembly document.
Shows the manipulator in this SOLIDWORKS part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Show( _
   ByVal PModelDoc As System.Object _
) 
```

```

Dim instance As IManipulator
Dim PModelDoc As System.Object
 
instance.Show(PModelDoc)
```

```

void Show( 
   System.object PModelDoc
)
```

```

void Show( 
   System.Object^ PModelDoc
) 
```

#### Parameters

*PModelDoc*
:   [Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)

Example

[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)  
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)  
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.md)  
[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.md)
