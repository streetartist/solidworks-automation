# GetLoopCount Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoopCount`

Gets the number of loops in this face.
Gets the number of loops in this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLoopCount() As System.Integer
```

```

Dim instance As IFace2
Dim value As System.Integer
 
value = instance.GetLoopCount()
```

```

System.int GetLoopCount()
```

```

System.int GetLoopCount(); 
```

#### Return Value

Number of loops in this face

Remarks

Call this method before calling [IFace2::IGetLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops.md) to determine the size of the array for that method.

Example

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Get Loops (VBA)](Get_Loops_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[IFace2::GetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFirstLoop.md)  
[IFace2::IGetFirstLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFirstLoop.md)  
[ILoop2::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~GetNext.md)  
[ILoop2::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IGetNext.md)  
[IFace2::GetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetLoops.md)  
[IFace2::IGetLoops Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetLoops.md)
