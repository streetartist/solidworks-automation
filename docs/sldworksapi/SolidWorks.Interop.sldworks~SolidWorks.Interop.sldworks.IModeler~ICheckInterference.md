# ICheckInterference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference`

Obsolete. Superseded by IModeler::ICheckInterference2.
Obsolete. Superseded by [IModeler::ICheckInterference2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICheckInterference( _
   ByRef Body1InterferedFaceArray As Face, _
   ByRef Body2InterferedFaceArray As Face, _
   ByRef IntersectedBodyArray As Body _
) 
```

```

Dim instance As IModeler
Dim Body1InterferedFaceArray As Face
Dim Body2InterferedFaceArray As Face
Dim IntersectedBodyArray As Body
 
instance.ICheckInterference(Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

```

void ICheckInterference( 
   out Face Body1InterferedFaceArray,
   out Face Body2InterferedFaceArray,
   out Body IntersectedBodyArray
)
```

```

void ICheckInterference( 
   [Out] Face^ Body1InterferedFaceArray,
   [Out] Face^ Body2InterferedFaceArray,
   [Out] Body^ IntersectedBodyArray
) 
```

#### Parameters

*Body1InterferedFaceArray*

*Body2InterferedFaceArray*

*IntersectedBodyArray*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
