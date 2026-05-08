# IGetFirstFaceArray Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetFirstFaceArray`

Obsolete. Superseded by IMidSurface2::IGetFirstFaceArray.
Obsolete. Superseded by [IMidSurface2::IGetFirstFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFaceArray.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstFaceArray( _
   ByVal FromFrontFaceListDisp As System.IntPtr, _
   ByRef SizeOfFrontFaceList As System.Integer, _
   ByVal FromFaceBackListDisp As System.IntPtr, _
   ByRef SizeOfBackFaceList As System.Integer, _
   ByRef Thickness As System.Double _
) As Face
```

```

Dim instance As IMidSurface
Dim FromFrontFaceListDisp As System.IntPtr
Dim SizeOfFrontFaceList As System.Integer
Dim FromFaceBackListDisp As System.IntPtr
Dim SizeOfBackFaceList As System.Integer
Dim Thickness As System.Double
Dim value As Face
 
value = instance.IGetFirstFaceArray(FromFrontFaceListDisp, SizeOfFrontFaceList, FromFaceBackListDisp, SizeOfBackFaceList, Thickness)
```

```

Face IGetFirstFaceArray( 
   out System.IntPtr FromFrontFaceListDisp,
   out System.int SizeOfFrontFaceList,
   out System.IntPtr FromFaceBackListDisp,
   out System.int SizeOfBackFaceList,
   out System.double Thickness
)
```

```

Face^ IGetFirstFaceArray( 
   [Out] System.IntPtr FromFrontFaceListDisp,
   [Out] System.int SizeOfFrontFaceList,
   [Out] System.IntPtr FromFaceBackListDisp,
   [Out] System.int SizeOfBackFaceList,
   [Out] System.double Thickness
) 
```

#### Parameters

*FromFrontFaceListDisp*

*SizeOfFrontFaceList*

*FromFaceBackListDisp*

*SizeOfBackFaceList*

*Thickness*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.md)  
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.md)
