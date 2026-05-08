# ICreateBodyFromFaces2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces2`

Obsolete. Superseded by IModeler::ICreateBodyFromFace3.
Obsolete. Superseded by [IModeler::ICreateBodyFromFace3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodyFromFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef Faces As Face, _
   ByVal ActionType As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) As Body
```

```

Dim instance As IModeler
Dim NumOfFaces As System.Integer
Dim Faces As Face
Dim ActionType As System.Integer
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
Dim value As Body
 
value = instance.ICreateBodyFromFaces2(NumOfFaces, Faces, ActionType, DoLocalCheck, LocalCheckResult)
```

```

Body ICreateBodyFromFaces2( 
   System.int NumOfFaces,
   ref Face Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   out System.bool LocalCheckResult
)
```

```

Body^ ICreateBodyFromFaces2( 
   System.int NumOfFaces,
   Face^% Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   [Out] System.bool LocalCheckResult
) 
```

#### Parameters

*NumOfFaces*

*Faces*

*ActionType*

*DoLocalCheck*

*LocalCheckResult*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
