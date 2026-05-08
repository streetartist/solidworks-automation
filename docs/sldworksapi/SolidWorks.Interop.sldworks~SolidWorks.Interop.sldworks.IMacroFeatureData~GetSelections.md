# GetSelections Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections`

Obsolete. Superseded by IMacroFeatureData::GetSelections3.
Obsolete. Superseded by [IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSelections( _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Object, _
   ByRef SelMarks As System.Object _
) 
```

```

Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim ObjectTypes As System.Object
Dim SelMarks As System.Object
 
instance.GetSelections(Objects, ObjectTypes, SelMarks)
```

```

void GetSelections( 
   out System.object Objects,
   out System.object ObjectTypes,
   out System.object SelMarks
)
```

```

void GetSelections( 
   [Out] System.Object^ Objects,
   [Out] System.Object^ ObjectTypes,
   [Out] System.Object^ SelMarks
) 
```

#### Parameters

*Objects*

*ObjectTypes*

*SelMarks*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
