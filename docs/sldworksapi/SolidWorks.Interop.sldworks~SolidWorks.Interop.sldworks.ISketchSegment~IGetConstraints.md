# IGetConstraints Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraints`

Gets the constraints for this sketch segment.
Gets the constraints for this sketch segment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConstraints() As System.String
```

```

Dim instance As ISketchSegment
Dim value As System.String
 
value = instance.IGetConstraints()
```

```

System.string IGetConstraints()
```

```

System.String^ IGetConstraints(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of sketch segment constraints (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The available constraint values are as follows:

|  |  |  |
| --- | --- | --- |
| - sgHORIZONTAL - sgHORIZPOINTS - sgVERTICAL - sgVERTPOINTS - sgCOLINEAR - sgCORADIAL - sgPERPENDICULAR - sgPARALLEL - sgTANGENT - sgCONCENTRIC - sgCOINCIDENT | - sgSYMMETRIC - sgATMIDDLE - sgATINTERSECT - sgATPIERCE - sgFIXED  - sgANGLE - sgARCANG180 - sgARCANG270 - sgARCANG90 - sgARCANGBOTTOM - sgARCANGLEFT | - sgARCANGRIGHT - sgARCANGTOP - sgDIAMETER - sgDISTANCE - sgSAMELENGTH - sgOFFSETEDGE - sgSNAPANGLE - sgSNAPGRID - sgSNAPLENGTH - sgUSEEDGE - sgMERGEPOINTS |

Example

[Get Sketch Segment Constraints (C++)](Get_Sketch_Segment_Constraints_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)  
[ISketchSegment::GetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetConstraints.md)  
[ISketchSegment::IGetConstraintsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraintsCount.md)  
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.md)
