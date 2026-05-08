# IGetNextFaceArray Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFaceArray`

Obsolete. Superseded by IMidSurface3::IGetNextFaceArray.
Obsolete. Superseded by [IMidSurface3::IGetNextFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFaceArray.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNextFaceArray( _
   ByRef FromFrontFaceListDisp As Face2, _
   ByRef SizeOfFrontFaceList As System.Integer, _
   ByRef FromFaceBackListDisp As Face2, _
   ByRef SizeOfBackFaceList As System.Integer, _
   ByRef Thickness As System.Double _
) As Face2
```

```

Dim instance As IMidSurface2
Dim FromFrontFaceListDisp As Face2
Dim SizeOfFrontFaceList As System.Integer
Dim FromFaceBackListDisp As Face2
Dim SizeOfBackFaceList As System.Integer
Dim Thickness As System.Double
Dim value As Face2
 
value = instance.IGetNextFaceArray(FromFrontFaceListDisp, SizeOfFrontFaceList, FromFaceBackListDisp, SizeOfBackFaceList, Thickness)
```

```

Face2 IGetNextFaceArray( 
   out Face2 FromFrontFaceListDisp,
   out System.int SizeOfFrontFaceList,
   out Face2 FromFaceBackListDisp,
   out System.int SizeOfBackFaceList,
   out System.double Thickness
)
```

```

Face2^ IGetNextFaceArray( 
   [Out] Face2^ FromFrontFaceListDisp,
   [Out] System.int SizeOfFrontFaceList,
   [Out] Face2^ FromFaceBackListDisp,
   [Out] System.int SizeOfBackFaceList,
   [Out] System.double Thickness
) 
```

#### Parameters

*FromFrontFaceListDisp*
:   List of front [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*SizeOfFrontFaceList*
:   Number of front faces

*FromFaceBackListDisp*
:   List of back [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*SizeOfBackFaceList*
:   Number of back faces

*Thickness*
:   Thickness between the faces

#### Return Value

Next [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

A separator is needed between the front faces and back faces. Thus, a NULL always exists between the front faces and the back faces.

For example, if there are five faces in the model, then the mid-surface has five faces. To get the five faces:

- Call [IMidSurface2::IGetGetFirstFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFaceArray.md) once.
- Call IMidSurface2::IGetNextFaceArray four times.

At each call, the data is arranged as follows if there is one front face in the array:  

[Neutral face], [front face], NULL, [back face]

If there are more than one front face in the array, then the data is arranged as follows:

[Neutral face], [front face1, front face2], NULL, [back face1, back face2]

Call [IMidSurface2::IGetFirstFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFaceArray.md) to get the first face from the original paired faces.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::GetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFaceArray.md)  
[IMidSurface2::GetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFaceArray.md)  
[IMidSurface2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFaceCount.md)
