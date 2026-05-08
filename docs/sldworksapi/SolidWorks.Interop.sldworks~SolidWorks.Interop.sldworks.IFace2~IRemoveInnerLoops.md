# IRemoveInnerLoops Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveInnerLoops`

Removes the inner loops on this face if the face is from a sheet (surface) body.
Removes the inner loops on this face if the face is from a sheet (surface) body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IRemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByRef InnerLoopsIn As Loop2 _
) As Face2
```

```

Dim instance As IFace2
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As Loop2
Dim value As Face2
 
value = instance.IRemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

```

Face2 IRemoveInnerLoops( 
   System.int NumOfLoops,
   ref Loop2 InnerLoopsIn
)
```

```

Face2^ IRemoveInnerLoops( 
   System.int NumOfLoops,
   Loop2^% InnerLoopsIn
) 
```

#### Parameters

*NumOfLoops*
:   Number of loops to remove

*InnerLoopsIn*
:   Pointer to an array of  the inner [loops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) to be removed

#### Return Value

Pointer to the resulting [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::RemoveInnerLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops.md)  
[IFace2::EnumLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumLoops.md)  
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.md)  
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.md)  
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.md)
