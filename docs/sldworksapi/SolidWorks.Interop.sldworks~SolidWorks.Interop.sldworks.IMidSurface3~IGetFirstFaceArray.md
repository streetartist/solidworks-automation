# IGetFirstFaceArray Method (IMidSurface3)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFaceArray`

Gets the first face and the thickness between the faces.
Gets the first face and the thickness between the faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstFaceArray( _
   ByRef FromFrontFaceListDisp As Face2, _
   ByRef SizeOfFrontFaceList As System.Integer, _
   ByRef FromFaceBackListDisp As Face2, _
   ByRef SizeOfBackFaceList As System.Integer, _
   ByRef Thickness As System.Double _
) As Face2
```

```

Dim instance As IMidSurface3
Dim FromFrontFaceListDisp As Face2
Dim SizeOfFrontFaceList As System.Integer
Dim FromFaceBackListDisp As Face2
Dim SizeOfBackFaceList As System.Integer
Dim Thickness As System.Double
Dim value As Face2
 
value = instance.IGetFirstFaceArray(FromFrontFaceListDisp, SizeOfFrontFaceList, FromFaceBackListDisp, SizeOfBackFaceList, Thickness)
```

```

Face2 IGetFirstFaceArray( 
   out Face2 FromFrontFaceListDisp,
   out System.int SizeOfFrontFaceList,
   out Face2 FromFaceBackListDisp,
   out System.int SizeOfBackFaceList,
   out System.double Thickness
)
```

```

Face2^ IGetFirstFaceArray( 
   [Out] Face2^ FromFrontFaceListDisp,
   [Out] System.int SizeOfFrontFaceList,
   [Out] Face2^ FromFaceBackListDisp,
   [Out] System.int SizeOfBackFaceList,
   [Out] System.double Thickness
) 
```

#### Parameters

*FromFrontFaceListDisp*
:   - in-process, unmanaged C++: Pointer to an array of front [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    :   - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*SizeOfFrontFaceList*
:   Number of front faces

*FromFaceBackListDisp*
:   - in-process, unmanaged C++: Pointer to an array of back [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*SizeOfBackFaceList*
:   :   Number of back faces

*Thickness*
:   Thickness between the faces

#### Return Value

First [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

A separator is needed between the front faces and back faces. Thus, a NULL always exists between the front faces and the back faces.

For example, if there are five faces in the model, then the mid-surface has five faces. To get the five faces:

- Call IMidSurface3::IGetGetFirstFaceArray once.
- Call [IMidSurface3::IGetNextFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFaceArray.md) four times.

At each call, the data is arranged as follows if there is one front face in the array:  

[Neutral face], [front face], NULL, [back face]

If there are more than one front face in the array, then the data is arranged as follows:

[Neutral face], [front face1, front face2], NULL, [back face1, back face2]

To get the next face from the original paired faces, call IMidSurface3::IGetNextFaceArray.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md)  
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.md)  
[IMidSurface3::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaceCount.md)  
[IMidSurface3::GetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFaceArray.md)  
[IMidSurface3::GetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFaceArray.md)  
[IMidSurface3::IGetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFaceArray.md)
