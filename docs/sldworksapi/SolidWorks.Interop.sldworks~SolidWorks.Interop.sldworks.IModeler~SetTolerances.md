# SetTolerances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetTolerances`

Obsolete. Superseded by IModeler::GetToleranceValue and IModeler::SetToleranceValue.
Obsolete. Superseded by [IModeler::GetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.md) and [IModeler::SetToleranceValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTolerances( _
   ByRef ToleranceIDArray As System.Integer, _
   ByRef ToleranceValueArray As System.Double, _
   ByVal NumTol As System.Integer _
) As System.Boolean
```

```

Dim instance As IModeler
Dim ToleranceIDArray As System.Integer
Dim ToleranceValueArray As System.Double
Dim NumTol As System.Integer
Dim value As System.Boolean
 
value = instance.SetTolerances(ToleranceIDArray, ToleranceValueArray, NumTol)
```

```

System.bool SetTolerances( 
   ref System.int ToleranceIDArray,
   ref System.double ToleranceValueArray,
   System.int NumTol
)
```

```

System.bool SetTolerances( 
   System.int% ToleranceIDArray,
   System.double% ToleranceValueArray,
   System.int NumTol
) 
```

#### Parameters

*ToleranceIDArray*
:   Type of tolerance you want to set as defined in [swTolerances\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)

*ToleranceValueArray*
:   New tolerance value in meters for the specified tolerance type

*NumTol*
:   Original value of the specified tolerance type

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
