# CreateGroup Method (ISMNormalCutFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~CreateGroup`

Creates a group of connected faces to cut.
Creates a group of connected faces to cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateGroup( _
   ByRef ErrCode As System.Integer _
) As System.Object
```

```

Dim instance As ISMNormalCutFeatureData2
Dim ErrCode As System.Integer
Dim value As System.Object
 
value = instance.CreateGroup(ErrCode)
```

```

System.object CreateGroup( 
   out System.int ErrCode
)
```

```

System.Object^ CreateGroup( 
   [Out] System.int ErrCode
) 
```

#### Parameters

*ErrCode*
:   Error code as defined in [swNormalCutErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutErrors_e.html)

#### Return Value

[ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.md)

Example

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md)  
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)
