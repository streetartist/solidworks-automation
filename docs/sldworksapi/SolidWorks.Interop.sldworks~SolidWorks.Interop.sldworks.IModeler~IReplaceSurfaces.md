# IReplaceSurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces`

Obsolete. Superseded by IModeler::IReplaceSurfaces2.
Obsolete. Superseded by [IModeler::IReplaceSurfaces2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IReplaceSurfaces( _
   ByVal NFaces As System.Integer, _
   ByRef FaceArray As Face, _
   ByRef NewSurfArray As Surface, _
   ByRef SenseArray As System.Integer, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

```

Dim instance As IModeler
Dim NFaces As System.Integer
Dim FaceArray As Face
Dim NewSurfArray As Surface
Dim SenseArray As System.Integer
Dim Tolerance As System.Double
Dim value As System.Boolean
 
value = instance.IReplaceSurfaces(NFaces, FaceArray, NewSurfArray, SenseArray, Tolerance)
```

```

System.bool IReplaceSurfaces( 
   System.int NFaces,
   ref Face FaceArray,
   ref Surface NewSurfArray,
   ref System.int SenseArray,
   System.double Tolerance
)
```

```

System.bool IReplaceSurfaces( 
   System.int NFaces,
   Face^% FaceArray,
   Surface^% NewSurfArray,
   System.int% SenseArray,
   System.double Tolerance
) 
```

#### Parameters

*NFaces*

*FaceArray*

*NewSurfArray*

*SenseArray*

*Tolerance*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
