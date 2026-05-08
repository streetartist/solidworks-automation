# AddMate Method (IMoveCopyBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~AddMate`

Adds a mate to the feature.
Adds a mate to the feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddMate( _
   ByVal MateEntVar As System.Object, _
   ByVal MateTypeFromEnum As System.Integer, _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal Angle As System.Double, _
   ByRef ErrorStatus As System.Integer _
) As Mate2
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim MateEntVar As System.Object
Dim MateTypeFromEnum As System.Integer
Dim AlignFromEnum As System.Integer
Dim Distance As System.Double
Dim Angle As System.Double
Dim ErrorStatus As System.Integer
Dim value As Mate2
 
value = instance.AddMate(MateEntVar, MateTypeFromEnum, AlignFromEnum, Distance, Angle, ErrorStatus)
```

```

Mate2 AddMate( 
   System.object MateEntVar,
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.double Distance,
   System.double Angle,
   out System.int ErrorStatus
)
```

```

Mate2^ AddMate( 
   System.Object^ MateEntVar,
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.double Distance,
   System.double Angle,
   [Out] System.int ErrorStatus
) 
```

#### Parameters

*MateEntVar*
:   Array of the entities to use to create a mate (see **Remarks**)

*MateTypeFromEnum*
:   Type of mate as defined in [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html)

*AlignFromEnum*
:   Type of alignment as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)

*Distance*
:   Distance to use with distance or limit mates

*Angle*
:   Angle to use with angle mates

*ErrorStatus*
:   Success or error as defined by [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

#### Return Value

[Mate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

You can specify MateEntVar with either an array of mate entities or null. If you specify null, then before calling this method, you must call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a selection mark of 1 to select each mate entity.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)  
[IMoveCopyBodyFeatureData::IAddMate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IAddMate.md)
