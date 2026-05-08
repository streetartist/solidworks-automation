# GetConstraints Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetConstraints`

Gets the constraints for this sketch segment.
Gets the constraints for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetConstraints() As System.Object
```

```

Dim instance As ISketchSegment
Dim value As System.Object
 
value = instance.GetConstraints()
```

```

System.object GetConstraints()
```

```

System.Object^ GetConstraints(); 
```

#### Return Value

Array of sketch segment constraints (see **Remarks**)

Remarks

The available constraint values are as follows:

|  |  |  |
| --- | --- | --- |
| - sgHORIZONTAL - sgHORIZPOINTS - sgVERTICAL - sgVERTPOINTS - sgCOLINEAR - sgCORADIAL - sgPERPENDICULAR - sgPARALLEL - sgTANGENT - sgCONCENTRIC - sgCOINCIDENT | - sgSYMMETRIC - sgATMIDDLE - sgATINTERSECT - sgATPIERCE - sgFIXED  - sgANGLE - sgARCANG180 - sgARCANG270 - sgARCANG90 - sgARCANGBOTTOM - sgARCANGLEFT | - sgARCANGRIGHT - sgARCANGTOP - sgDIAMETER - sgDISTANCE - sgSAMELENGTH - sgOFFSETEDGE - sgSNAPANGLE - sgSNAPGRID - sgSNAPLENGTH - sgUSEEDGE - sgMERGEPOINTS |

Example

[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::IGetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraints.md)  
[ISketchSegment::IGetConstraintsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraintsCount.md)  
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.md)
