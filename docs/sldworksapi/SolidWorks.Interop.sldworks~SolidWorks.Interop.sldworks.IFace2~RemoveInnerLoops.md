# RemoveInnerLoops Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveInnerLoops`

Removes the inner loops on this face if the face is from a sheet (surface) body.
Removes the inner loops on this face if the face is from a sheet (surface) body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveInnerLoops( _
   ByVal NumOfLoops As System.Integer, _
   ByVal InnerLoopsIn As System.Object _
) As System.Object
```

```

Dim instance As IFace2
Dim NumOfLoops As System.Integer
Dim InnerLoopsIn As System.Object
Dim value As System.Object
 
value = instance.RemoveInnerLoops(NumOfLoops, InnerLoopsIn)
```

```

System.object RemoveInnerLoops( 
   System.int NumOfLoops,
   System.object InnerLoopsIn
)
```

```

System.Object^ RemoveInnerLoops( 
   System.int NumOfLoops,
   System.Object^ InnerLoopsIn
) 
```

#### Parameters

*NumOfLoops*
:   Number of loops to remove

*InnerLoopsIn*
:   Array of the inner loops to remove

#### Return Value

Resulting [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::IRemoveInnerLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveInnerLoops.md)  
[IFace2::EnumLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~EnumLoops.md)  
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.md)  
[IFace2::GetLoopCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount.md)  
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.md)
