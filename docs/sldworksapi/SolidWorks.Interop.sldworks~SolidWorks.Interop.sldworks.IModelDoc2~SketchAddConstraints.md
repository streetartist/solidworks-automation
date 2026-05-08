# SketchAddConstraints Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchAddConstraints`

Adds the specified constraint to the selected entities.
Adds the specified constraint to the selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchAddConstraints( _
   ByVal IdStr As System.String _
) 
```

```

Dim instance As IModelDoc2
Dim IdStr As System.String
 
instance.SketchAddConstraints(IdStr)
```

```

void SketchAddConstraints( 
   System.string IdStr
)
```

```

void SketchAddConstraints( 
   System.String^ IdStr
) 
```

#### Parameters

*IdStr*
:   Constraint (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **SOLIDWORKS 2005 and earlier** | **SOLIDWORKS 2006 and later** |
| - sgHORIZONTAL (2D sketch) - sgHORIZONTAL (3D sketch) - sgHORIZPOINTS (2D sketch) - sgHORIZPOINTS (3D sketch) - sgVERTICAL (2D sketch) - sgVERTICAL (3D sketch) - sgVERTPOINTS (2D sketch) - sgVERTPOINTS (3D sketch) - sgALONGZPOINTS - sgALONGZ - sgCOLINEAR - sgCORADIAL - sgPERPENDICULAR - sgPARALLEL - sgTANGENT - sgCONCENTRIC - sgCOINCIDENT - sgSYMMETRIC - sgATMIDDLE - sgATINTERSECT - sgATPIERCE - sgFIXED - sgANGLE - sgARCANG180 - sgARCANG270 - sgARCANG90 - sgARCANGBOTTOM - sgARCANGLEFT - sgARCANGRIGHT - sgARCANGTOP - sgDIAMETER - sgDISTANCE - sgSAMELENGTH - sgOFFSETEDGE - sgSNAPANGLE - sgSNAPGRID - sgSNAPLENGTH - sgUSEEDGE | - sgHORIZONTAL2D - sgALONGX3D - sgHORIZONTALPOINTS2D - sgALONGXPOINTS3D - sgVERTICAL2D - sgALONGY3D - sgVERTICALPOINTS2D - sgALONGYPOINTS3D - sgALONGZPOINTS3D - sgALONGZ3D - sgCOLINEAR - sgCORADIAL - sgPERPENDICULAR - sgPARALLEL - sgTANGENT - sgCONCENTRIC - sgCOINCIDENT - sgSYMMETRIC - sgATMIDDLE - sgATINTERSECT - sgATPIERCE - sgFIXED - sgANGLE - sgARCANG180 - sgARCANG270 - sgARCANG90 - sgARCANGBOTTOM - sgARCANGLEFT - sgARCANGRIGHT - sgARCANGTOP - sgDIAMETER - sgDISTANCE - sgSAMELENGTH - sgOFFSETEDGE - sgSNAPANGLE - sgSNAPGRID - sgSNAPLENGTH - sgUSEEDGE - sgMERGEPOINTS |

Example

[Constrain Sketch (VBA)](Constrain_Sketch_Example_VB.htm)  
[Constrain Sketch (VB.NET)](Constrain_Sketch_Example_VBNET.htm)  
[Constrain Sketch (C#)](Constrain_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchConstrainCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainCoincident.md)  
[IModelDoc2::SketchConstrainConcentric Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainConcentric.md)  
[IModelDoc2::SketchConstrainParallel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainParallel.md)  
[IModelDoc2::SketchConstrainPerp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainPerp.md)  
[IModelDoc2::SketchConstrainTangent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainTangent.md)  
[IModelDoc2::SketchConstraintsDel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDel.md)  
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.md)  
[IModelDoc2::ViewConstraint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewConstraint.md)  
[IModelDoc2::SkToolsAutoConstr Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SkToolsAutoConstr.md)
