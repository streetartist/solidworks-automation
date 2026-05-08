# ReplaceSurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ReplaceSurfaces`

Replaces the surfaces of the given faces.
Replaces the surfaces of the given faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceSurfaces( _
   ByVal NFaces As System.Integer, _
   ByVal FaceArray As System.Object, _
   ByVal NewSurfArray As System.Object, _
   ByVal SenseArray As System.Object, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

```

Dim instance As IModeler
Dim NFaces As System.Integer
Dim FaceArray As System.Object
Dim NewSurfArray As System.Object
Dim SenseArray As System.Object
Dim Tolerance As System.Double
Dim value As System.Boolean
 
value = instance.ReplaceSurfaces(NFaces, FaceArray, NewSurfArray, SenseArray, Tolerance)
```

```

System.bool ReplaceSurfaces( 
   System.int NFaces,
   System.object FaceArray,
   System.object NewSurfArray,
   System.object SenseArray,
   System.double Tolerance
)
```

```

System.bool ReplaceSurfaces( 
   System.int NFaces,
   System.Object^ FaceArray,
   System.Object^ NewSurfArray,
   System.Object^ SenseArray,
   System.double Tolerance
) 
```

#### Parameters

*NFaces*
:   Number of faces to have surfaces replaced

*FaceArray*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to have the surfaces replaced

*NewSurfArray*
:   Array of [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) to be replaced in these faces

*SenseArray*
:   Array of the senses of each surface in NewSurfArray

*Tolerance*
:   Tolerance

#### Return Value

True if operation is successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::IReplaceSurfaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces2.md)
