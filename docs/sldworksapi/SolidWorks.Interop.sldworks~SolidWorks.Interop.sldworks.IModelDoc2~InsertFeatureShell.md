# InsertFeatureShell Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShell`

Creates a shell feature.
Creates a shell feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertFeatureShell( _
   ByVal Thickness As System.Double, _
   ByVal Outward As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Thickness As System.Double
Dim Outward As System.Boolean
 
instance.InsertFeatureShell(Thickness, Outward)
```

```

void InsertFeatureShell( 
   System.double Thickness,
   System.bool Outward
)
```

```

void InsertFeatureShell( 
   System.double Thickness,
   System.bool Outward
) 
```

#### Parameters

*Thickness*
:   Shell thickness in meters

*Outward*
:   True for outside, false for inside

Remarks

Before calling this method, select faces to remove to create the shell using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Marks of 1. See the SOLIDWORKS Help for information about what entities are valid for selection.

To make a multi-thickness shell, use this method with [IModelDoc2::InsertFeatureShellAddThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFeatureShellAddThickness.md).

Example

[Create Shell Feature (VBA)](Get_Shell_Feature_Data_Example_VB.htm)  
[Create Shell Feature (VB.NET)](Create_Shell_Feature_Example_VBNET.htm)  
[Create Shell Feature (C#)](Create_Shell_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IShellFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData.md)
