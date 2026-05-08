# GetModifiedInstances Method (IInstanceToVaryOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedInstances`

Gets instance numbers of modified pattern instances of the specified type.
Gets instance numbers of modified pattern instances of the specified type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModifiedInstances( _
   ByVal ModificationType As System.Integer _
) As System.Object
```

```

Dim instance As IInstanceToVaryOptions
Dim ModificationType As System.Integer
Dim value As System.Object
 
value = instance.GetModifiedInstances(ModificationType)
```

```

System.object GetModifiedInstances( 
   System.int ModificationType
)
```

```

System.Object^ GetModifiedInstances( 
   System.int ModificationType
) 
```

#### Parameters

*ModificationType*
:   Modification type as defined by [swInstanceToVaryModificationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInstanceToVaryModificationType_e.html)

#### Return Value

Array of pattern instance numbers

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md)  
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.md)  
[IInstanceToVaryOptions::GetModifiedDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedDimensions.md)  
[IInstanceToVaryOptions::GetD1ModifiedSpacingValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD1ModifiedSpacingValue.md)  
[IInstanceToVaryOptions::GetD2ModifiedSpacingValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD2ModifiedSpacingValue.md)
