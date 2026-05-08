# ChangeSketchPlane Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ChangeSketchPlane`

Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations.
Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ChangeSketchPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.ChangeSketchPlane(Config_opt, Config_names)
```

```

System.bool ChangeSketchPlane( 
   System.int Config_opt,
   System.object Config_names
)
```

```

System.bool ChangeSketchPlane( 
   System.int Config_opt,
   System.Object^ Config_names
) 
```

#### Parameters

*Config\_opt*
:   Configurations as defined by [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names

#### Return Value

True if the operation succeeds, false if it fails

Remarks

Every sketch is associated with a plane (for example, a reference plane or a planar face). You must preselect the sketch and the new plane or face before using this method.

Example

[Change Plane of Sketch (VBA)](Change_Sketch_Plane_Example_VB.htm)  
[Change Plane of Sketch (VB.NET)](Change_Sketch_of_Plane_Example_VBNET.htm)  
[Change Plane of Sketch (C#)](Change_Sketch_of_Plane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::IChangeSketchPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IChangeSketchPlane.md)
