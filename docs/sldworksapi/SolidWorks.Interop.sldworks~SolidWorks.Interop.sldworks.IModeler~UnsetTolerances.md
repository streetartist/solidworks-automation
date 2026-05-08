# UnsetTolerances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~UnsetTolerances`

Sets the tolerances back to system settings.
Sets the tolerances back to system settings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UnsetTolerances( _
   ByRef ToleranceIDArray As System.Integer, _
   ByVal NumTol As System.Integer _
) As System.Boolean
```

```

Dim instance As IModeler
Dim ToleranceIDArray As System.Integer
Dim NumTol As System.Integer
Dim value As System.Boolean
 
value = instance.UnsetTolerances(ToleranceIDArray, NumTol)
```

```

System.bool UnsetTolerances( 
   ref System.int ToleranceIDArray,
   System.int NumTol
)
```

```

System.bool UnsetTolerances( 
   System.int% ToleranceIDArray,
   System.int NumTol
) 
```

#### Parameters

*ToleranceIDArray*
:   Array specifying the tolerances to reset as defined in [swTolerances\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolerances_e.html)

*NumTol*
:   Number of tolerance types you are resetting; this value should correspond to the number of elements in the ToleranceIDArray array

#### Return Value

True if the tolerances is reset successfully, false if n

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::GetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~GetToleranceValue.md)  
[IModeler::SetToleranceValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SetToleranceValue.md)
