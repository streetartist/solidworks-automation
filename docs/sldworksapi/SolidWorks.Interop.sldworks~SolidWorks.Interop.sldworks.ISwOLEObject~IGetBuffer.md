# IGetBuffer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBuffer`

Gets the data for this OLE object.
Gets the data for this OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetBuffer( _
   ByVal OleBufferSize As System.Integer, _
   ByRef BOleData As System.Byte _
) 
```

```

Dim instance As ISwOLEObject
Dim OleBufferSize As System.Integer
Dim BOleData As System.Byte
 
instance.IGetBuffer(OleBufferSize, BOleData)
```

```

void IGetBuffer( 
   System.int OleBufferSize,
   out System.byte BOleData
)
```

```

void IGetBuffer( 
   System.int OleBufferSize,
   [Out] System.byte BOleData
) 
```

#### Parameters

*OleBufferSize*
:   Size of the OLE buffer

*BOleData*
:   Byte array for the buffer data

Remarks

Before calling this method, call [ISwOLEObject::BufferSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~BufferSize.md) to get the value for OleBufferSize.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)  
[ISwOLEObject::Buffer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Buffer.md)
