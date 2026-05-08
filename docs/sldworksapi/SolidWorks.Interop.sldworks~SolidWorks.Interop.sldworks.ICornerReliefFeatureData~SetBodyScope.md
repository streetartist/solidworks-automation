# SetBodyScope Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~SetBodyScope`

Sets the sheet metal body to which this corner relief feature is applied.
Sets the sheet metal body to which this corner relief feature is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBodyScope( _
   ByVal SheetBody As System.Object _
) As System.Integer
```

```

Dim instance As ICornerReliefFeatureData
Dim SheetBody As System.Object
Dim value As System.Integer
 
value = instance.SetBodyScope(SheetBody)
```

```

System.int SetBodyScope( 
   System.object SheetBody
)
```

```

System.int SetBodyScope( 
   System.Object^ SheetBody
) 
```

#### Parameters

*SheetBody*
:   [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) sheet metal body

#### Return Value

Error code as defined by [swCornerReliefError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)
