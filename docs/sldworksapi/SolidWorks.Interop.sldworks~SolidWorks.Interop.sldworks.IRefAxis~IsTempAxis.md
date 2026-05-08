# IsTempAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~IsTempAxis`

Gets whether the reference axis is a temporary axis.
Gets whether the reference axis is a temporary axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTempAxis() As System.Boolean
```

```

Dim instance As IRefAxis
Dim value As System.Boolean
 
value = instance.IsTempAxis()
```

```

System.bool IsTempAxis()
```

```

System.bool IsTempAxis(); 
```

#### Return Value

True if the reference axis is a temporary axis, false if not

Example

[Get Temporary Axis and Its Reference Face (C#)](Get_Temporary_Axis_and_Its_Reference_Face_Example_CSharp.htm)  
[Get Temporary Axis and Its Reference Face (VB.NET)](Get_Temporary_Axis_and_Its_Reference_Face_Example_VBNET.htm)  
[Get Temporary Axis and Its Reference Face (VBA)](Get_Temporary_Axis_and_Its_Reference_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefAxis Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)  
[IRefAxis Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.md)  
[IRefAxis::GetTempAxisReferenceFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis~GetTempAxisReferenceFace.md)
