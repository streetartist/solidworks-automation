# GetNextFaceArray Method (IMidSurface3)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFaceArray`

Gets the next face from the original paired faces and the thickness between the faces.
Gets the next face from the original paired faces and the thickness between the faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNextFaceArray( _
   ByRef Thickness As System.Double _
) As System.Object
```

```

Dim instance As IMidSurface3
Dim Thickness As System.Double
Dim value As System.Object
 
value = instance.GetNextFaceArray(Thickness)
```

```

System.object GetNextFaceArray( 
   out System.double Thickness
)
```

```

System.Object^ GetNextFaceArray( 
   [Out] System.double Thickness
) 
```

#### Parameters

*Thickness*
:   :   Thickness between the faces

#### Return Value

Next [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

A separator is needed between the front faces and back faces. Thus, a NULL always exists between the front faces and the back faces.

For example, if there are five faces in the model, then the mid-surface has five faces. To get the five faces:

- Call [IMidSurface3::GetGetFirstFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFaceArray.md) once.
- Call IMidSurface2::GetNextFaceArray four times.

At each call, the data is arranged as follows if there is one front face in the array:  

[Neutral face], [front face], NULL, [back face]

If there are more than one front face in the array, then the data is arranged as follows:

[Neutral face], [front face1, front face2], NULL, [back face1, back face2]

Call [IMidSurface3::GetFirstFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFaceArray.md) to get the first face from the original paired faces.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.md)  
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.md)  
[IMidSurface3::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaceCount.md)  
[IMidSurface3::GetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFaceArray.md)  
[IMidSurface3::IGetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFaceArray.md)  
[IMidSurface3::IGetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFaceArray.md)
