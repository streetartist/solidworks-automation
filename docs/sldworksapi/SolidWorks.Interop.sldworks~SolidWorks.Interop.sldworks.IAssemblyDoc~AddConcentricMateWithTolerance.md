# AddConcentricMateWithTolerance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance`

Adds a misaligned concentric mate to this assembly.
Adds a misaligned concentric mate to this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddConcentricMateWithTolerance( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal ConcentricPositionType As System.Integer, _
   ByVal ConcentricToleranceCheck As System.Boolean, _
   ByVal ConcentricToleranceValue As System.Double, _
   ByRef ErrorStatus As System.Integer _
) As Mate2
```

```

Dim instance As IAssemblyDoc
Dim AlignFromEnum As System.Integer
Dim ConcentricPositionType As System.Integer
Dim ConcentricToleranceCheck As System.Boolean
Dim ConcentricToleranceValue As System.Double
Dim ErrorStatus As System.Integer
Dim value As Mate2
 
value = instance.AddConcentricMateWithTolerance(AlignFromEnum, ConcentricPositionType, ConcentricToleranceCheck, ConcentricToleranceValue, ErrorStatus)
```

```

Mate2 AddConcentricMateWithTolerance( 
   System.int AlignFromEnum,
   System.int ConcentricPositionType,
   System.bool ConcentricToleranceCheck,
   System.double ConcentricToleranceValue,
   out System.int ErrorStatus
)
```

```

Mate2^ AddConcentricMateWithTolerance( 
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

#### Return Value

Misaligned concentric [mate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

Select the two entities to mate before calling this method. A parent non-misaligned (i.e., standard) concentric mate must already exist between the selected entities. If a suitable parent concentric mate does not exist between the selected entities, then a standard concentric mate is created.

**NOTE:** The typical way to add a standard concentric mate is to use [IAssemblyDoc::AddMate5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.md).

Example

[Add and Edit Misaligned Symmetric Concentric Mate (VBA)](Add_and_Edit_Misaligned_Symmetric_Concentric_Mate_Example_VB.htm)  
[Add and Edit Misaligned Symmetric Concentric Mate (VB.NET)](Add_and_Edit_Misaligned_Symmetric_Concentric_Mate_Example_VBNET.htm)  
[Add and Edit Misaligned Symmetric Concentric Mate (C#)](Add_and_Edit_Misaligned_Symmetric_Concentric_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::EditConcentricMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditConcentricMate.md)  
[IAssemblyDoc::EditMate4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate4.md)
