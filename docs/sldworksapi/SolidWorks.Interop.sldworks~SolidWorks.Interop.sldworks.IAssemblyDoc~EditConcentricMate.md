# EditConcentricMate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditConcentricMate`

Edits a misaligned concentric mate.
Edits a misaligned concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditConcentricMate( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal ConcentricPositionType As System.Integer, _
   ByVal ConcentricToleranceCheck As System.Boolean, _
   ByVal ConcentricToleranceValue As System.Double, _
   ByRef ErrorStatus As System.Integer _
) 
```

```

Dim instance As IAssemblyDoc
Dim AlignFromEnum As System.Integer
Dim ConcentricPositionType As System.Integer
Dim ConcentricToleranceCheck As System.Boolean
Dim ConcentricToleranceValue As System.Double
Dim ErrorStatus As System.Integer
 
instance.EditConcentricMate(AlignFromEnum, ConcentricPositionType, ConcentricToleranceCheck, ConcentricToleranceValue, ErrorStatus)
```

```

void EditConcentricMate( 
   System.int AlignFromEnum,
   System.int ConcentricPositionType,
   System.bool ConcentricToleranceCheck,
   System.double ConcentricToleranceValue,
   out System.int ErrorStatus
)
```

```

void EditConcentricMate( 
   System.int AlignFromEnum,
   System.int ConcentricPositionType,
   System.bool ConcentricToleranceCheck,
   System.double ConcentricToleranceValue,
   [Out] System.int ErrorStatus
) 
```

#### Parameters

*AlignFromEnum*
:   Type of mate alignment as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)

*ConcentricPositionType*
:   Misaligned concentric mate position as defined in [swConcentricAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html)

*ConcentricToleranceCheck*
:   True to override the deviation, false to have SOLIDWORKS calculate the deviation

*ConcentricToleranceValue*
:   Maximum deviation; valid only when ConcentricToleranceCheck is true

*ErrorStatus*
:   Success or error as defined by [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

Remarks

Select these entities before calling this method:

- Two entities that define the misaligned concentric mate
- Misaligned concentric mate

A parent non-misaligned (i.e., standard) concentric mate must already exist for the selected misaligned concentric mate. If a suitable parent concentric mate does not exist, then the selected misaligned concentric mate changes to a standard concentric mate. You can also change a misaligned concentric mate to a standard concentric mate using [IAssemblyDoc::EditMate4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate4.md).

After calling IAssemblyDoc::EditConcentricMate, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

Example

See the [IAssemblyDoc::AddConcentricMateWithTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddConcentricMateWithTolerance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.md)  
[IAssemblyDoc::AddMate5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.md)
