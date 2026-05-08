# CreateMateData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMateData`

Creates a mate feature data object for the specified mate type.
Creates a mate feature data object for the specified mate type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateMateData( _
   ByVal Type As System.Integer _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.CreateMateData(Type)
```

```

System.object CreateMateData( 
   System.int Type
)
```

```

System.Object^ CreateMateData( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Type of mate to create as defined in [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html) (see **Remarks**)

#### Return Value

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md)

Remarks

Type must be one of the following mate types as defined in swMateType\_e:

- swMateANGLE
- swMateCAMFOLLOWER
- swMateCOINCIDENT
- swMateCONCENTRIC
- swMateDISTANCE
- swMateGEAR
- swMateHINGE
- swMateLINEARCOUPLER
- swMateLOCK
- swMatePARALLEL
- swMatePERPENDICULAR
- swMatePROFILECENTER
- swMateRACKPINION
- swMateSCREW
- swMateSLOT
- swMateSYMMETRIC
- swMateTANGENT
- swMateUNIVERSALJOINT
- swMateWIDTH

To create a mate, see the [IAssemblydoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks section.

Example

See [IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AutoMateRepair Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoMateRepair.md)
