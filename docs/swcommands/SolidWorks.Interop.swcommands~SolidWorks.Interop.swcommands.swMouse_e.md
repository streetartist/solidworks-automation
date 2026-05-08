# swMouse_e Enumeration

Help ID: `SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swMouse_e`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS API Commands Enumeration | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands.swMouse_e.html) on this topic. |
| swMouse\_e Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swcommands Namespace](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands_namespace.md) : swMouse\_e Enumeration |

Visual Basic (Declaration)
  

C#
  

C++/CLI

Mouse commands.

# Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum swMouse_e     Inherits System.Enum ``` | |

| C# |  |
| --- | --- |
| ``` public enum swMouse_e : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class swMouse_e : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swMouse\_Absolute** | 256 or 0x100 |
| **swMouse\_Click** | 512 or 0x200 |
| **swMouse\_DoubleClick** | 1024 or 0x400 |
| **swMouse\_LeftDown** | 2 or 0x2 |
| **swMouse\_LeftUp** | 4 or 0x4 |
| **swMouse\_MiddleDoubleClick** | 8192 or 0x2000; Zoom to fit |
| **swMouse\_MiddleDown** | 32 or 0x20 |
| **swMouse\_MiddleUp** | 64 or 0x40 |
| **swMouse\_MouseMove** | 1 or 0x1 |
| **swMouse\_RightClick** | 2048 or 0x800 |
| **swMouse\_RightDoubleClick** | 4096 or 0x1000 |
| **swMouse\_RightDown** | 8 or 0x8 |
| **swMouse\_RightUp** | 16 or 0x10 |
| **swMouse\_SelectANNOTATIONTABLES** | 0x620000; filters mouse selections to annotation tables |
| **swMouse\_SelectANNOTATIONVIEW** | 0x8b0000; filters mouse selections to annotation views |
| **swMouse\_SelectARROWS** | 0x310000; filters mouse selections to arrows |
| **swMouse\_SelectATTRIBUTES** | 0x80000; filters mouse selections to attributes |
| **swMouse\_SelectBLOCKDEF** | 0x630000; filters mouse selections to block definitions |
| **swMouse\_SelectBLOCKINST** | 0x5d0000; filters mouse selections to block instances |
| **swMouse\_SelectBODYFEATURES** | 0x160000; filters mouse selections to body features |
| **swMouse\_SelectBODYFOLDER** | 0x760000; filters mouse selections to body folders |
| **swMouse\_SelectBOMFEATURES** | 0x610000; filters mouse selections to BOM features |
| **swMouse\_SelectBOMS** | 0x360000; filters mouse selections to BOMs |
| **swMouse\_SelectBOMTEMPS** | 0x400000; filters mouse selections to BOM templates |
| **swMouse\_SelectBorder** | 0xfe0000; filters mouse selections to borders |
| **swMouse\_SelectBREAKLINES** | 0x1f0000; filters mouse selections to breaklines |
| **swMouse\_SelectBROWSERITEM** | 0x450000; filters mouse selections to browser items |
| **swMouse\_SelectCAMERAS** | 0x880000; filters mouse selections to cameras |
| **swMouse\_SelectCENTERLINES** | 0x670000; filters mouse selections to centerlines |
| **swMouse\_SelectCENTERMARKS** | 0x1c0000; filters mouse selections to centermarks |
| **swMouse\_SelectCENTERMARKSYMS** | 0x640000; filters mouse selections to centermark symbols only |
| **swMouse\_SelectCOMMENT** | 0x7f0000; filters mouse selections to comments |
| **swMouse\_SelectCOMMENTSFOLDER** | 0x7e0000; filters mouse selections to comment folders |
| **swMouse\_SelectCOMPONENTS** | 0x140000; filters mouse selections to components |
| **swMouse\_SelectCOMPPATTERN** | 0x250000; filters mouse selections to component patterns |
| **swMouse\_SelectCOMPSDONTOVERRIDE** | 0x480000; filters mouse selections to specified selection types (e.g., edges, vertices, or faces) over the competing component selection type in an assembly |
| **swMouse\_SelectCONFIGURATIONS** | 0x2f0000; filters mouse selections to configurations |
| **swMouse\_SelectCONNECTIONPOINTS** | 0x420000; filters mouse selections to connection points |
| **swMouse\_SelectCOORDSYS** | 0x3d0000; filters mouse selections to coordinate systems |
| **swMouse\_SelectCOSMETICWELDS** | 0xdc0000; filters mouse selections to cosmetic welds |
| **swMouse\_SelectCTHREADS** | 0x270000; filters mouse selections to cosmetic threads |
| **swMouse\_SelectCUSTOMSYMBOLS** | 0x3c0000; filters mouse selections to custom symbols |
| **swMouse\_SelectDATUMAXES** | 0x50000; filters mouse selections to datum axes |
| **swMouse\_SelectDATUMLINES** | 0x3e0000; filters mouse selections to datum lines |
| **swMouse\_SelectDATUMPLANES** | 0x40000; filters mouse selections to datum planes |
| **swMouse\_SelectDATUMPOINTS** | 0x60000; filters mouse selections to datum points |
| **swMouse\_SelectDATUMTAGS** | 0x240000; filters mouse selections to datum tags |
| **swMouse\_SelectDCABINETS** | 0x2a0000; filters mouse selections to D cabinets |
| **swMouse\_SelectDETAILCIRCLES** | 0x110000; filters mouse selections to detail circles |
| **swMouse\_SelectDIMENSIONS** | 0xe0000; filters mouse selections to dimensions |
| **swMouse\_SelectDISPLAYSTATE** | 0x940000; filters mouse selections to display states |
| **swMouse\_SelectDOCSFOLDER** | 0x7d0000; filters mouse selections to document folders |
| **swMouse\_SelectDOWELSYMS** | 0x560000; filters mouse selections to dowel symbols |
| **swMouse\_SelectDRAWINGVIEWS** | 0xc0000; filters mouse selections to drawing views |
| **swMouse\_SelectDTMTARGS** | 0x280000; filters mouse selections to datum targets |
| **swMouse\_SelectEDGES** | 65536 or 0x10000; filters mouse selections to edges |
| **swMouse\_SelectEMBEDLINKDOC** | 0x7b0000; filters mouse selections to embedded document links |
| **swMouse\_SelectEMPTYSPACE** | 0x480000; filters mouse selections to empty spaces |
| **swMouse\_SelectEQNFOLDER** | 0x370000; filters mouse selections to equations folders |
| **swMouse\_SelectEXCLUDEMANIPULATORS** | 0x6f0000; filters mouse selections to exclude manipulators |
| **swMouse\_SelectEXPLLINES** | 0x2d0000; filters mouse selections to explode lines |
| **swMouse\_SelectEXPLSTEPS** | 0x2c0000; filters mouse selections to explode steps |
| **swMouse\_SelectEXPLVIEWS** | 0x2b0000; filters mouse selections to explode views |
| **swMouse\_SelectEXTSKETCHPOINTS** | 0x190000; filters mouse selections to sketch points |
| **swMouse\_SelectEXTSKETCHSEGS** | 0x180000; filters mouse selections to sketch segments |
| **swMouse\_SelectEXTSKETCHTEXT** | 0x580000; filters mouse selections to sketch text |
| **swMouse\_SelectFABRICATEDROUTE** | 0x460000; filters mouse selections to a fabricated routes |
| **swMouse\_SelectFACES** | 131072 or 0x20000; filters mouse selections to faces |
| **swMouse\_SelectFRAMEPOINT** | 0x4d0000; filters mouse selections to frame points |
| **swMouse\_SelectFTRFOLDER** | 0x5e0000; filters mouse selections to feature folders |
| **swMouse\_SelectGENERALTABLEFEAT** | 0x8e0000; filters mouse selections to general table features |
| **swMouse\_SelectGTOLS** | 0xd0000; filters mouse selections to Gtols |
| **swMouse\_SelectHELIX** | 0x1a0000; filters mouse selections to helixes |
| **swMouse\_SelectHOLESERIES** | 0x530000; filters mouse selections to hole series |
| **swMouse\_SelectHOLETABLEAXES** | 0x690000; filters mouse selections to hole table axes |
| **swMouse\_SelectHOLETABLEFEATS** | 0x680000; filters mouse selections to hole table features |
| **swMouse\_SelectIMPORTFOLDER** | 0x390000; filters mouse selections to import folders |
| **swMouse\_SelectINCONTEXTFEAT** | 0x1d0000; filters mouse selections to in-context features |
| **swMouse\_SelectINCONTEXTFEATS** | 0x200000; filters mouse selections to in-context features |
| **swMouse\_SelectJOURNAL** | 0x7c0000; filters mouse selections to journals |
| **swMouse\_SelectLEADERS** | 0x540000; filters mouse selections to leaders |
| **swMouse\_SelectLIGHTS** | 0x490000; filters mouse selections to lights |
| **swMouse\_SelectMAGNETICLINES** | 0xe10000; filters mouse selections to magnetic lines |
| **swMouse\_SelectMANIPULATORS** | 0x4f0000; filters mouse selections to manipulators |
| **swMouse\_SelectMATEGROUP** | 0x1e0000; filters mouse selections to mate groups |
| **swMouse\_SelectMATEGROUPS** | 0x210000; filters mouse selections to multiple mate groups |
| **swMouse\_SelectMATES** | 0x150000; filters mouse selections to mates |
| **swMouse\_SelectMATESUPPLEMENT** | 0x8a0000; filters mouse selections to mate supplemental faces |
| **swMouse\_SelectMIDPOINTS** | 0x3b0000; filters mouse selections to midpoints |
| **swMouse\_SelectNOTES** | 0xf0000; filters mouse selections to notes |
| **swMouse\_SelectOBJGROUP** | 0xcf0000; filters mouse selections to object groups |
| **swMouse\_SelectOBJHANDLES** | 0x300000; filters mouse selections to object handles |
| **swMouse\_SelectOLEITEMS** | 0x70000; filters mouse seletions to OLE items |
| **swMouse\_SelectPICTUREBODIES** | 0x500000; filters mouse selections to picture bodies |
| **swMouse\_SelectPLANESECTIONS** | 0xdb0000; filters mouse selections to plane sections |
| **swMouse\_SelectPOINTREFS** | 0x290000; filters mouse selections to point references |
| **swMouse\_SelectPOSGROUP** | 0x440000; filters mouse selections to mate reference folders |
| **swMouse\_SelectPUNCHTABLEFEATS** | 0xea0000; filters mouse selections to punch table features |
| **swMouse\_SelectREFCURVES** | 0x170000; filters mouse selections to reference curves |
| **swMouse\_SelectREFEDGES** | 0x330000; filters mouse selections to reference edges |
| **swMouse\_SelectREFERENCECURVES** | 0x1a0000; filters mouse selections to reference curves |
| **swMouse\_SelectREFFACES** | 0x340000; filters mouse selections to reference faces |
| **swMouse\_SelectREFSILHOUETTE** | 0x350000; filters mouse selections to reference silouettes |
| **swMouse\_SelectREFSURFACES** | 0x1b0000; filters mouse selections to reference surfaces |
| **swMouse\_SelectREVISIONCLOUDS** | 0xf00000; filters mouse selections to revision clouds |
| **swMouse\_SelectREVISIONTABLE** | 0x710000; filters mouse selections to revision tables |
| **swMouse\_SelectREVISIONTABLEFEAT** | 0x770000; filters mouse selections to revision table features |
| **swMouse\_SelectROUTECURVES** | 0x3f0000; filters mouse selections to route curves |
| **swMouse\_SelectROUTEPOINTS** | 0x410000; filters mouse selections to route points |
| **swMouse\_SelectROUTESWEEPS** | 0x430000; filters mouse selections to route sweeps |
| **swMouse\_SelectSECTIONLINES** | 0x100000; filters mouse selections to section lines |
| **swMouse\_SelectSECTIONTEXT** | 0x120000; filters mouse selections to section text |
| **swMouse\_SelectSELECTIONSETFOLDER** | 0x1020000; filters mouse selections to selection set folders |
| **swMouse\_SelectSELECTIONSETNODE** | 0x1030000; filters mouse selections to selection set nodes |
| **swMouse\_SelectSFSYMBOLS** | 0x230000; filters mouse selections to SF symbols |
| **swMouse\_SelectSHEETS** | 0x130000; filters mouse selections to sheets |
| **swMouse\_SelectSILHOUETTES** | 0x2e0000; filters mouse selections to silhouettes |
| **swMouse\_SelectSIMELEMENT** | 0x660000; filters mouse selections to simulation elements |
| **swMouse\_SelectSIMULATION** | 0x650000; filters mouse selections to simulation studies |
| **swMouse\_SelectSKETCHBITMAP** | 0x550000; filters mouse selections to sketch bitmaps |
| **swMouse\_SelectSKETCHCONTOUR** | 0x600000; filters mouse selections to sketch contours |
| **swMouse\_SelectSKETCHES** | 0x90000; filters mouse selections to sketches |
| **swMouse\_SelectSKETCHHATCH** | 0x380000; filters mouse selections to sketch hatches |
| **swMouse\_SelectSKETCHPOINTFEAT** | 0x470000; filters mouse selections to sketch point features |
| **swMouse\_SelectSKETCHPOINTS** | 0xb0000; filters mouse selections to sketch points |
| **swMouse\_SelectSKETCHREGION** | 0x5f0000; filters mouse selections to sketch regions |
| **swMouse\_SelectSKETCHSEGS** | 0xa0000; filters mouse selections to sketch segments |
| **swMouse\_SelectSKETCHTEXT** | 0x220000; filters mouse selections to sketch text |
| **swMouse\_SelectSOLIDBODIES** | 0x4c0000; filters mouse selections to solid bodies |
| **swMouse\_SelectSOLIDBODIESFIRST** | 0x510000; filters mouse selections to solid bodies over competing selection types (e.g., face, component) |
| **swMouse\_SelectSUBATOMFOLDER** | 0x790000; filters mouse selections to body folders |
| **swMouse\_SelectSUBSKETCHDEF** | 0x9a0000; filters mouse selections to sketch block definitions |
| **swMouse\_SelectSUBSKETCHINST** | 0x720000; filters mouse selections to sketch block instances |
| **swMouse\_SelectSUBWELDFOLDER** | 0x6b0000; filters mouse selections to sub-weldment folders |
| **swMouse\_SelectSURFACEBODIES** | 0x4b0000; filters mouse selections to surface bodies |
| **swMouse\_SelectSURFBODIESFIRST** | 0x4e0000; filters mouse selections to surface bodies over competing selection types (e.g., face, component) |
| **swMouse\_SelectSWIFTANNOTATIONS** | 0x820000; filters mouse selections to Swift annotations |
| **swMouse\_SelectSWIFTFEATURES** | 0x840000; filters mouse selections to Swift features |
| **swMouse\_SelectSWIFTSCHEMA** | 0x9f0000; filters mouse selections to Swift schemas |
| **swMouse\_SelectTITLEBLOCK** | 0xc00000; filters mouse selections to title blocks |
| **swMouse\_SelectTITLEBLOCKTABLEFEAT** | 0xce0000; filters mouse selections to title block table features |
| **swMouse\_SelectVERTICES** | 196608 or 0x30000; filters mouse selections to vertexes |
| **swMouse\_SelectVIEWERHYPERLINK** | 0x3a0000; filters mouse selections to viewer hyperlinks |
| **swMouse\_SelectWELDBEADS** | 0x7a0000; filters mouse selections to weld beads |
| **swMouse\_SelectWELDMENT** | 0x6a0000; filters mouse selections to weldments |
| **swMouse\_SelectWELDMENTTABLEFEATS** | 0x740000; filters mouse selections to weldment table features |
| **swMouse\_SelectWELDS** | 0x260000; filters mouse selections to welds |
| **swMouse\_SelectWIREBODIES** | 0x4a0000; filters mouse selections to wire bodies |
| **swMouse\_SelectZONES** | 0x320000; filters mouse selections to zones |
| **swMouse\_Wheel** | 128 or 0x80 |

# See Also

#### 

[SolidWorks.Interop.swcommands Namespace](SolidWorks.Interop.swcommands~SolidWorks.Interop.swcommands_namespace.md)
