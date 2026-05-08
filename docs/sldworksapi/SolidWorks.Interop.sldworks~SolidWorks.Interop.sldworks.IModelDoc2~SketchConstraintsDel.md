# SketchConstraintsDel Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDel`

Deletes the specified relationship (constraint) on the currently selected sketch item.
Deletes the specified relationship (constraint) on the currently selected sketch item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchConstraintsDel( _
   ByVal ConstrInd As System.Integer, _
   ByVal IdStr As System.String _
) 
```

```

Dim instance As IModelDoc2
Dim ConstrInd As System.Integer
Dim IdStr As System.String
 
instance.SketchConstraintsDel(ConstrInd, IdStr)
```

```

void SketchConstraintsDel( 
   System.int ConstrInd,
   System.string IdStr
)
```

```

void SketchConstraintsDel( 
   System.int ConstrInd,
   System.String^ IdStr
) 
```

#### Parameters

*ConstrInd*
:   Constraint number on the selected entity; 0-based index

*IdStr*
:   Constraint to delete (see **Remarks**)

Remarks

To delete a tangency relation, which is the third relation on the selected arc, specify:

Part.SketchConstraintsDel 2, "sgTANGENT"

The available constraints are as follows. Pass them as strings embedded in quotes:

|  |  |
| --- | --- |
| **SOLIDWORKS 2005 and earlier** | **SOLIDWORKS 2006 and later** |
| - sgHORIZONTAL (2D sketch) | - sgHORIZONTAL2D |
| - sgHORIZONTAL (3D sketch) | - sgALONGX3D |
| - sgHORIZPOINTS (2D sketch) | - sgHORIZONTALPOINTS2D |
| - sgHORIZPOINTS (3D sketch) | - sgALONGXPOINTS3D |
| - sgVERTICAL (2D sketch) | - sgVERTICAL2D |
| - sgVERTICAL (3D sketch) | - sgALONGY3D |
| - sgVERTPOINTS (2D sketch) | - sgVERTICALPOINTS2D |
| - sgVERTPOINTS (3D sketch) | - sgALONGYPOINTS3D |
| - sgALONGZPOINTS - sgALONGZ - sgCOLINEAR - sgCORADIAL - sgPERPENDICULAR - sgPARALLEL - sgTANGENT - sgCONCENTRIC - sgCOINCIDENT - sgSYMMETRIC - sgATMIDDLE - sgATINTERSECT - sgATPIERCE - sgFIXED - sgANGLE - sgARCANG180 - sgARCANG270 - sgARCANG90 - sgARCANGBOTTOM - sgARCANGLEFT - sgARCANGRIGHT - sgARCANGTOP - sgDIAMETER - sgDISTANCE - sgSAMELENGTH - sgOFFSETEDGE - sgSNAPANGLE - sgSNAPGRID - sgSNAPLENGTH - sgUSEEDGE | - sgALONGZPOINTS3D - sgALONGZ3D - sgCOLINEAR - sgCORADIAL - sgPERPENDICULAR - sgPARALLEL - sgTANGENT - sgCONCENTRIC - sgCOINCIDENT - sgSYMMETRIC - sgATMIDDLE - sgATINTERSECT - sgATPIERCE - sgFIXED - sgANGLE - sgARCANG180 - sgARCANG270 - sgARCANG90 - sgARCANGBOTTOM - sgARCANGLEFT - sgARCANGRIGHT - sgARCANGTOP - sgDIAMETER - sgDISTANCE - sgSAMELENGTH - sgOFFSETEDGE - sgSNAPANGLE - sgSNAPGRID - sgSNAPLENGTH - sgUSEEDGE - sgMERGEPOINTS |

NOTE: Although SOLIDWORKS 2006 and later accepts the constraints shown in the first column, you are encouraged to use the constraints shown in the second column.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchAddConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchAddConstraints.md)  
[IModelDoc2::SketchConstrainCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainCoincident.md)  
[IModelDoc2::SketchConstrainConcentric Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainConcentric.md)  
[IModelDoc2::SketchConstrainParallel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainParallel.md)  
[IModelDoc2::SketchConstrainPerp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainPerp.md)  
[IModelDoc2::SketchConstrainTangent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainTangent.md)  
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.md)  
[IModelDoc2::SkToolsAutoConstr Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SkToolsAutoConstr.md)
