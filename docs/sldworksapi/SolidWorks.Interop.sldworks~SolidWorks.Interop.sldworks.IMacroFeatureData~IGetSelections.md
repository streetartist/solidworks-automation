# IGetSelections Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections`

Obsolete. Superseded by IMacroFeatureData::IGetSelections3.
Obsolete. Superseded by [IMacroFeatureData::IGetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetSelections( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Integer, _
   ByRef SelMarks As System.Integer _
) 
```

```

Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim ObjectTypes As System.Integer
Dim SelMarks As System.Integer
 
instance.IGetSelections(SelCount, Objects, ObjectTypes, SelMarks)
```

```

void IGetSelections( 
   System.int SelCount,
   out System.object Objects,
   out System.int ObjectTypes,
   out System.int SelMarks
)
```

```

void IGetSelections( 
   System.int SelCount,
   [Out] System.Object^ Objects,
   [Out] System.int ObjectTypes,
   [Out] System.int SelMarks
) 
```

#### Parameters

*SelCount*

*Objects*

*ObjectTypes*

*SelMarks*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
