# ISetSelections Method (IMacroFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections`

Obsolete. Superseded by IMacroFeatureData::ISetSelections2.
Obsolete. Superseded by [IMacroFeatureData::ISetSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSelections( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef SelMarks As System.Integer _
) 
```

```

Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim SelMarks As System.Integer
 
instance.ISetSelections(SelCount, Objects, SelMarks)
```

```

void ISetSelections( 
   System.int SelCount,
   ref System.object Objects,
   ref System.int SelMarks
)
```

```

void ISetSelections( 
   System.int SelCount,
   System.Object^% Objects,
   System.int% SelMarks
) 
```

#### Parameters

*SelCount*

*Objects*

*SelMarks*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
