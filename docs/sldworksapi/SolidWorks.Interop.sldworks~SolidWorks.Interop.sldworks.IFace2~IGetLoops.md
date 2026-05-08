# IGetLoops Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops`

Gets all of the loops on this face.
Gets all of the loops on this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetLoops( _
   ByVal NumberOfLoops As System.Integer _
) As Loop2
```

```

Dim instance As IFace2
Dim NumberOfLoops As System.Integer
Dim value As Loop2
 
value = instance.IGetLoops(NumberOfLoops)
```

```

Loop2 IGetLoops( 
   System.int NumberOfLoops
)
```

```

Loop2^ IGetLoops( 
   System.int NumberOfLoops
) 
```

#### Parameters

*NumberOfLoops*
:   Number of loops on the face

#### Return Value

- in-process, unmanaged C++: Pointer to an array of all of the [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) on the face (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IFace2::GetLoopCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.md) to get NumberOfLoops.

If a face has one or more holes on it, then this method gets a loop for the face and a loop for every hole on the face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoops.md)  
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.md)  
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.md)  
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.md)  
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.md)
