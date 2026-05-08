# IDeleteFaces3 Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDeleteFaces3`

Obsolete. Superseded by IBody2::IDeleteFaces3.
Obsolete. Superseded by [IBody2::IDeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFaces3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IDeleteFaces3( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByVal Option As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) 
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim Option As System.Integer
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
 
instance.IDeleteFaces3(NumOfFaces, FaceList, Option, DoLocalCheck, LocalCheckResult)
```

```

void IDeleteFaces3( 
   System.int NumOfFaces,
   ref Face FaceList,
   System.int Option,
   System.bool DoLocalCheck,
   ref System.bool LocalCheckResult
)
```

```

void IDeleteFaces3( 
   System.int NumOfFaces,
   Face^% FaceList,
   System.int Option,
   System.bool DoLocalCheck,
   System.bool% LocalCheckResult
) 
```

#### Parameters

*NumOfFaces*

*FaceList*

*Option*

*DoLocalCheck*

*LocalCheckResult*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
