# ICheckInterference2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference2`

Obsolete. Superseded by IModeler::ICheckInterference3.
Obsolete. Superseded by [IModeler::ICheckInterference3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICheckInterference2( _
   ByRef Body1InterferedFaceArray As Face2, _
   ByRef Body2InterferedFaceArray As Face2, _
   ByRef IntersectedBodyArray As Body2 _
) 
```

```

Dim instance As IModeler
Dim Body1InterferedFaceArray As Face2
Dim Body2InterferedFaceArray As Face2
Dim IntersectedBodyArray As Body2
 
instance.ICheckInterference2(Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

```

void ICheckInterference2( 
   out Face2 Body1InterferedFaceArray,
   out Face2 Body2InterferedFaceArray,
   out Body2 IntersectedBodyArray
)
```

```

void ICheckInterference2( 
   [Out] Face2^ Body1InterferedFaceArray,
   [Out] Face2^ Body2InterferedFaceArray,
   [Out] Body2^ IntersectedBodyArray
) 
```

#### Parameters

*Body1InterferedFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfered from the first body with the second body

*Body2InterferedFaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that interfered from the second body with the first body

*IntersectedBodyArray*
:   [Bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) generated from the intersection of the input bodies

Remarks

Before calling this method, call [IModeler::ICheckInterferenceCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterferenceCount2.md) to allocate memory for the arrays returned from this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CheckInterference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterference.md)  
[IAssembyDoc::IToolsCheckInterference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.md)  
[IAssembyDoc::ToolsCheckInterference2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ToolsCheckInterference2.md)
