# ICreateBodyFromFaces Method (IModeler)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces`

Obsolete. Superseded by IModeler::ICreateBodyFromFace3.
Obsolete. Superseded by [IModeler::ICreateBodyFromFace3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodyFromFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByRef Faces As Face, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) As Body
```

```

Dim instance As IModeler
Dim NumOfFaces As System.Integer
Dim Faces As Face
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
Dim value As Body
 
value = instance.ICreateBodyFromFaces(NumOfFaces, Faces, DoLocalCheck, LocalCheckResult)
```

```

Body ICreateBodyFromFaces( 
   System.int NumOfFaces,
   ref Face Faces,
   System.bool DoLocalCheck,
   ref System.bool LocalCheckResult
)
```

```

Body^ ICreateBodyFromFaces( 
   System.int NumOfFaces,
   Face^% Faces,
   System.bool DoLocalCheck,
   System.bool% LocalCheckResult
) 
```

#### Parameters

*NumOfFaces*

*Faces*

*DoLocalCheck*

*LocalCheckResult*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
