# GetSelections2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections2`

Obsolete. Superseded by IMacroFeatureData::GetSelections3.
Obsolete. Superseded by [IMacroFeatureData::GetSelections3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSelections2( _
   ByRef Objects As System.Object, _
   ByRef ObjectTypes As System.Object, _
   ByRef SelMarks As System.Object, _
   ByRef DrViews As System.Object _
) 
```

```

Dim instance As IMacroFeatureData
Dim Objects As System.Object
Dim ObjectTypes As System.Object
Dim SelMarks As System.Object
Dim DrViews As System.Object
 
instance.GetSelections2(Objects, ObjectTypes, SelMarks, DrViews)
```

```

void GetSelections2( 
   out System.object Objects,
   out System.object ObjectTypes,
   out System.object SelMarks,
   out System.object DrViews
)
```

```

void GetSelections2( 
   [Out] System.Object^ Objects,
   [Out] System.Object^ ObjectTypes,
   [Out] System.Object^ SelMarks,
   [Out] System.Object^ DrViews
) 
```

#### Parameters

*Objects*

*ObjectTypes*

*SelMarks*

*DrViews*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
